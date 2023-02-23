# Baekjoon 크롤러 작성 완료
from typing import List
import aiohttp
import asyncio
import sys


class BaekjoonScrapper:
    """
    Solved.ac api를 활용한 데이터 수집
    """
    BAEKJOON_BASE_URL = "https://solved.ac/api/v3"
    BAEKJOON_QUERY = {"problem/show": "?problemId="}

    async def fetch(session, url, headers):
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                result = await response.json()
                return result

    def unit_api(self, query: str, id: str) -> dict:
        """
        api 사용에 필요한 URL, header 정보 설정
        """
        return {
            "url": f"{self.BAEKJOON_BASE_URL}/{query}{self.BAEKJOON_QUERY[query]}{id}",
            "headers": {
                "Content-Type": "application/json",
            }
        }

    async def get_problem(self, problem_id: List) -> List[dict]:
        """
        문제 번호(problem_id)를 통해, 문제 정보 크롤링
        """
        apis = [self.unit_api("problem/show", id) for id in problem_id]
        async with aiohttp.ClientSession() as session:
            all_data = await asyncio.gather(
                *[BaekjoonScrapper.fetch(session, api["url"], api["headers"]) for api in apis]
            )
            # 결과 저장
            result = []
            for data in all_data:
                if data is not None:
                    result.append(data)
            return result

    def run(self, query: str, ids: List[str]):
        if query == "problem/show":
            return asyncio.run(self.get_problem(ids))


if __name__ == "__main__":
    baekjoon = BaekjoonScrapper()
    # Windows의 aiohttp 오류 방지
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    results = baekjoon.run("problem/show", ["1000", "1001"])
    print(results[0]["problemId"], results[1]["problemId"])