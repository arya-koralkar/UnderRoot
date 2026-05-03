# Contributing to UnderRoot

Thank you for contributing to UnderRoot! Please follow these guidelines to keep our codebase clean and our collaboration smooth.

## Git Workflow

We use **GitHub Flow**:

1. Fork the repository
2. Create a feature branch from `main`
3. Make your changes
4. Open a Pull Request

## Branch Naming

| Type | Pattern | Example |
|------|---------|---------|
| Feature | `feat/<short-description>` | `feat/citation-export` |
| Bug fix | `fix/<short-description>` | `fix/collab-reconnect` |
| Documentation | `docs/<short-description>` | `docs/api-reference` |
| Chore | `chore/<short-description>` | `chore/update-deps` |

## Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short summary>

[optional body]
```

Examples:
- `feat(citation): add IEEE format export`
- `fix(collab): handle reconnect on token expiry`
- `docs(setup): add manual setup instructions`

## Pull Request Process

1. Ensure your branch is up to date with `main`
2. Fill in the PR template
3. Request review from at least one team member
4. Address all review comments
5. Squash commits before merging

## Code Style

- **Frontend**: Follow ESLint + Prettier config
- **Backend**: Follow TypeScript strict mode
- **AI Service**: Follow PEP 8 + type hints required

## Running Tests

```bash
# Frontend
cd frontend && npm test

# Backend
cd backend && npm test

# AI Service
cd ai-service && pytest
```
