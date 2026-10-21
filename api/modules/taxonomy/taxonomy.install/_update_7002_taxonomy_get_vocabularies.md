# _update_7002_taxonomy_get_vocabularies()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.install`](_file.md), lines 271–273 · [local source](../../../../source/modules/taxonomy/taxonomy.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install#L271-L273)
- **Module/theme:** taxonomy
- **Topics:** [update_api](../../../topics/update_api.md)

## Signature

```php
function _update_7002_taxonomy_get_vocabularies()
```

## Documentation

```text
Utility function: get the list of vocabularies directly from the database.

This function is valid for a database schema version 7002.

@ingroup update_api
```

## Code

```php
function _update_7002_taxonomy_get_vocabularies() {
  return db_query('SELECT v.* FROM {taxonomy_vocabulary} v ORDER BY v.weight, v.name')->fetchAllAssoc('vid', PDO::FETCH_OBJ);
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.install](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install) · Licensed GPL-2.0-or-later (see LICENSE)._
