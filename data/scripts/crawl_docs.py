import os
import json
from pathlib import Path
from typing import List, Dict
import git


def clone_triton_repo(repo_url: str, target_dir: str) -> None:
    """
    Triton 레포지토리를 클론합니다.
    """
    try:
        repo = git.Repo(target_dir)
    except:
        repo = git.Repo.clone_from(repo_url, target_dir)
    repo.remote().pull()
    print("pulling triton repo is done.")


def collect_markdown_files(docs_dir: str) -> List[str]:
    """
    docs 디렉토리에서 모든 .md 파일 경로를 수집합니다.
    """
    md_files = []
    for path, _, files in os.walk(docs_dir):
        for filename in files:
            if filename.endswith(".md"):
                md_files.append(os.path.join(path, filename))
    return md_files


def extract_metadata_from_path(file_path: str, repo_root: str) -> Dict:
    """
    파일 경로에서 메타데이터를 추출합니다.
    Phase 1 - 파일 명에서 최소 정보만 추출(섹션, 제목)
    """
    path_obj = Path(file_path)
    relative_path = path_obj.relative_to(repo_root)

    # 기본 정보
    metadata = {
        "source_type": "documentation",
        "file_path": str(relative_path),
        "url": f"https://github.com/triton-inference-server/server/blob/main/{relative_path}",
    }

    # 섹션 추출 (docs/user_guide/model_repository.md -> user_guide)
    parts = relative_path.parts
    if len(parts) > 2 and parts[0] == "docs":
        metadata["section"] = parts[1]

    # 파일명에서 제목 추정
    metadata["title"] = path_obj.stem.replace("_", " ").title()

    return metadata


if __name__ == "__main__":
    REPO_URL = "https://github.com/triton-inference-server/server.git"
    TARGET_DIR = "data/raw/triton-server"

    # 실행
    clone_triton_repo(REPO_URL, TARGET_DIR)
    md_files = collect_markdown_files(os.path.join(TARGET_DIR, "docs"))

    print(f"총 {len(md_files)}개의 마크다운 파일 발견")
    for f in md_files[:5]:
        print(f"  - {f}")
