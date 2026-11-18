# Mini-Sistema de Videojuegos en Flask (PracticaJuegosORM)

[![CI - Pruebas Unitarias y Cobertura](https://github.com/jonathanaceves2766-debug/PracticaJuegosORM/actions/workflows/ci.yml/badge.svg)](https://github.com/jonathanaceves2766-debug/PracticaJuegosORM/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/jonathanaceves2766-debug/PracticaJuegosORM/branch/main/graph/badge.svg)](https://codecov.io/gh/jonathanaceves2766-debug/PracticaJuegosORM)

Proyecto desarrollado en Flask y SQLAlchemy para la gestion de videojuegos con pruebas unitarias automatizadas mediante `pytest`, reporte de cobertura con `pytest-cov` e integracion continua en GitHub Actions.

## Ejecucion local de pruebas y cobertura

```bash
pip install -r requirements.txt
pytest --cov=. --cov-report=term-missing
```
