import re
from typing import Optional, Dict

def parse_problem_dir_name(name: str) -> tuple[Optional[str], str]:
    m = re.match(r"(\d+)-(.+)", name)
    if m:
        return m.group(1), m.group(2)
    return None, name

def parse_submission_filename(fn: str) -> Dict[str, str]:
    fn = fn.replace(".py", "")
    m = re.match(
        r"(?P<date>\d{4}-\d{2}-\d{2} \d{2}\.\d{2}\.\d{2}) - (?P<status>[^-]+) - runtime (?P<runtime>[^-]+) - memory (?P<memory>[^ ]+)",
        fn
    )
    if not m:
        return {}
    date_str = m.group("date").replace(".", ":")
    return {
        "submitted_at": date_str,
        "status": m.group("status").strip(),
        "runtime": m.group("runtime").strip(),
        "memory": m.group("memory").strip(),
    }

def parse_problem_statement(md_path: str) -> Optional[str]:
    try:
        with open(md_path, encoding="utf-8") as f:
            first_line = f.readline().strip()
            if first_line.startswith("#"):
                return first_line.lstrip("#").strip()
    except Exception:
        pass
    return None

def parse_problem_difficulty(md_path: str) -> Optional[str]:
    try:
        with open(md_path, encoding="utf-8") as f:
            first_line = f.readline()
            m = re.search(r"Difficulty:\s*(\w+)", first_line)
            if m:
                return m.group(1)
    except Exception:
        pass
    return None

def parse_runtime(runtime_str: str) -> Optional[float]:
    """Parse a runtime string like '150ms' into a float milliseconds.

    Returns None if parsing fails or the string is empty.
    """
    if not runtime_str:
        return None
    try:
        # Some dumps include units like "ms" or "ms*"; strip everything but
        # digits and decimal point.
        num = "".join(ch for ch in runtime_str if ch.isdigit() or ch == ".")
        return float(num)
    except Exception:
        return None


def parse_memory(memory_str: str) -> Optional[float]:
    """Parse a memory string like '28.1MB' into a float megabytes.

    Returns None if parsing fails or the string is empty.
    """
    if not memory_str:
        return None
    try:
        num = "".join(ch for ch in memory_str if ch.isdigit() or ch == ".")
        return float(num)
    except Exception:
        return None
