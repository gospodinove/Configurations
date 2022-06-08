# Raycast

Storage for config back-ups and custom scripts

## Balance

In order to use the `balance` script, you need to do two things:

1. Provide a JSON file calles `balance-credentials.json` containing your Spendee credentials:

```JSON
{
  "email": "john@doe.com",
  "password": "your password"
}
```

2. Install the Spendee Python API wrapper

```Bash
pip install spendee
```

## Shell back up

In order to install the backed up data:

-   Brew

```Bash
brew bundle install --file=[path/to/backup]

```

-   Node

```Bash
xargs npm install --global < [path/to/backup]
```
