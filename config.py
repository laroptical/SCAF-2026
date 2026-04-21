from dataclasses import dataclass

@dataclass
class Config:
    data: str
    models: str
    llm: str
    rl: str
    conformal: str
    production: str
