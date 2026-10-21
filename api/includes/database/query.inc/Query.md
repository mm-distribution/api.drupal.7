# Query

- **Type:** Class
- **File:** [`includes/database/query.inc`](_file.md), lines 275–436 · [local source](../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L275-L436)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
abstract class Query implements QueryPlaceholderInterface
```

## Documentation

```text
Base class for query builders.

Note that query builders use PHP's magic __toString() method to compile the
query object into a prepared statement.
```

## Properties

### $connection

```php
protected $connection;
```

```text
The connection object on which to run this query.

@var DatabaseConnection
```

### $connectionTarget

```php
protected $connectionTarget;
```

```text
The target of the connection object.

@var string
```

### $connectionKey

```php
protected $connectionKey;
```

```text
The key of the connection object.

@var string
```

### $queryOptions

```php
protected $queryOptions;
```

```text
The query options to pass on to the connection object.

@var array
```

### $uniqueIdentifier

```php
protected $uniqueIdentifier;
```

```text
A unique identifier for this query object.
```

### $nextPlaceholder

```php
protected $nextPlaceholder = 0;
```

```text
The placeholder counter.
```

### $comments

```php
protected $comments = array();
```

```text
An array of comments that can be prepended to a query.

@var array
```

## Methods (derived index)

- [__construct()](Query/__construct.md) — Constructs a Query object.
- [__sleep()](Query/__sleep.md) — Implements the magic __sleep function to disconnect from the database.
- [__wakeup()](Query/__wakeup.md) — Implements the magic __wakeup function to reconnect to the database.
- [__clone()](Query/__clone.md) — Implements the magic __clone function.
- [execute()](Query/execute.md) — Runs the query against the database.
- [__toString()](Query/__toString.md) — Implements PHP magic __toString method to convert the query to a string.
- [uniqueIdentifier()](Query/uniqueIdentifier.md) — Returns a unique identifier for this object.
- [nextPlaceholder()](Query/nextPlaceholder.md) — Gets the next placeholder value for this query object.
- [comment()](Query/comment.md) — Adds a comment to the query.
- [getComments()](Query/getComments.md) — Returns a reference to the comments array for the query.

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
