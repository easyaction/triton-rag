import os
import json
from pathlib import Path
from typing import List, Dict
import git

def clone_triton_repo(repo_url: str, target_dir: str) -> None:
    """
    Triton 레포지토리를 클론합니다.
    
    TODO:
    1. git.Repo.clone_from()을 사용하여 레포지토리 클론
    2. 이미 존재하면 git pull로 업데이트
    3. 에러 처리 추가
    """
    pass

def collect_markdown_files(docs_dir: str) -> List[str]:
    """
    docs 디렉토리에서 모든 .md 파일 경로를 수집합니다.
    
    TODO:
    1. Path(docs_dir).rglob("*.md")로 재귀적으로 마크다운 파일 찾기
    2. 파일 경로 리스트 반환
    3. README.md는 포함, 숨김 파일(.으로 시작)은 제외
    """
    pass

def extract_metadata_from_path(file_path: str, repo_root: str) -> Dict:
    """
    파일 경로에서 메타데이터를 추출합니다.
    
    예: docs/user_guide/model_repository.md
    -> section: "user_guide", filename: "model_repository"
    
    TODO:
    1. 상대 경로 계산 (repo_root 기준)
    2. 디렉토리 구조에서 섹션 정보 추출
    3. 파일명에서 제목 추정 (snake_case -> Title Case)
    """
    pass

if __name__ == "__main__":
    REPO_URL = "https://github.com/triton-inference-server/server.git"
    TARGET_DIR = "data/raw/triton-server"
    
    # 실행
    clone_triton_repo(REPO_URL, TARGET_DIR)
    md_files = collect_markdown_files(os.path.join(TARGET_DIR, "docs"))
    
    print(f"총 {len(md_files)}개의 마크다운 파일 발견")
    for f in md_files[:5]:
        print(f"  - {f}")
