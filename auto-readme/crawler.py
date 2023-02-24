from typing import List, Dict
import aiohttp
import asyncio
import sys
from bs4 import BeautifulSoup
import re


class Problem:
    """
    Represents a problem from the platforms
    - id : 문제 고유 번호
    - title : 문제 이름
    - url : 사이트 내 문제 주소
    """

    def __init__(self, id: str, title: str, url: str):
        self.id = id
        self.title = title
        self.url = url


class BaekjoonScraper:
    """
    A web scraper for the Baekjoon Online Judge.
    """
    BASE_URL = "https://www.acmicpc.net"
    API_URL = "https://solved.ac/api/v3"

    async def fetch(self, session: aiohttp.ClientSession, url: str, headers: Dict[str, str]) -> str:
        """
        Sends an HTTP GET request using the specified session, URL, and headers.
        Returns the response body as json.
        """
        try:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    return await response.json()
        except aiohttp.ClientError:
            print(f"Failed to fetch{url}")

    async def get_problem(self, problem_id: str) -> Problem:
        """
        Fetches the details for a single problem, given its ID.
        Returns a Problem object representing the problem.
        """
        api_url = f"{BaekjoonScraper.API_URL}/problem/show?problemId={problem_id}"
        headers = {"Content-Type": "application/json"}
        async with aiohttp.ClientSession() as session:
            response_json = await self.fetch(session, api_url, headers)
            # 파일 정보 확인
            problem_title = response_json['titleKo']
            problem_url = f"{BaekjoonScraper.BASE_URL}/problem/{problem_id}"
            return Problem(problem_id, problem_title, problem_url)

    async def get_problems(self, problem_ids: List[str]) -> List[Problem]:
        """
        Fetches the details for multiple problems, given their IDs.
        Returns a list of Problem objects representing the problems.
        """
        tasks = [self.get_problem(id) for id in problem_ids]
        return await asyncio.gather(*tasks)


class ProgrammersScraper:
    """
    A web scraper for the Programmers.
    """
    BASE_URL = "https://programmers.co.kr/"
    API_URL = "https://school.programmers.co.kr/learn/courses/30/30-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%97%B0%EC%8A%B5"

    async def fetch(self, session: aiohttp.ClientSession, url: str, headers: Dict[str, str]) -> str:
        """
        Sends an HTTP GET request using the specified session, URL, and headers.
        Returns the response body as json.
        """
        try:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    return await response.text()
        except aiohttp.ClientError:
            print(f"Failed to fetch{url}")

    async def get_problems(self, problem_titles: List[str]) -> List[Problem]:
        """
        Fetches the details for a single problem, given its ID.
        Returns a Problem object representing the problem.
        """
        api_url = f"{ProgrammersScraper.API_URL}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50", }
        async with aiohttp.ClientSession() as session:
            response_html = await self.fetch(session, api_url, headers)
            soup = BeautifulSoup(response_html, "html.parser")
            problems = soup.select(".lesson-title")
            # 결과 저장
            result = []
            for problem in problems:
                problem_id = problem['href'].split("/")[-1]
                problem_title = re.sub(r"\s", "", problem.text)
                problem_url = f"{ProgrammersScraper.BASE_URL}{problem['href']}"
                if problem_title in problem_titles:
                    result.append(
                        Problem(problem_id, problem_title, problem_url))
            return result

# To - Do : Softeer 크롤러 구현하기


async def get_problems(problem_info=None):
    baekjoon_scraper = BaekjoonScraper()
    programmers_scraper = ProgrammersScraper()

    baekjoon_problem_ids = ["1000", "1001", "1002"]
    programmers_problem_titles = ["점의위치구하기", "배열의평균값"]

    tasks = [
        baekjoon_scraper.get_problems(baekjoon_problem_ids),
        programmers_scraper.get_problems(programmers_problem_titles)
    ]

    baekjoon_problems, programmers_problems = await asyncio.gather(*tasks)

    print(baekjoon_problems)
    print(programmers_problems[0].url)

if __name__ == "__main__":
    # Windows의 aiohttp 오류 방지
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(get_problems())