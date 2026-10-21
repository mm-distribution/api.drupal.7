# EntityFieldQuery::addTag()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 1153–1156 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L1153-L1156)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
public function addTag($tag)
```

## Documentation

```text
Adds a tag to the query.

Tags are strings that mark a query so that hook_query_alter() and
hook_query_TAG_alter() implementations may decide if they wish to alter
the query. A query may have any number of tags, and they must be valid PHP
identifiers (composed of letters, numbers, and underscores). For example,
queries involving nodes that will be displayed for a user need to add the
tag 'node_access', so that the node module can add access restrictions to
the query.

If an entity field query has tags, it must also have an entity type
specified, because the alter hook will need the entity base table.

@param string $tag
  The tag to add.

@return EntityFieldQuery
  The called object.
```

## Code

```php
  public function addTag($tag) {
    $this->tags[$tag] = $tag;
    return $this;
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
