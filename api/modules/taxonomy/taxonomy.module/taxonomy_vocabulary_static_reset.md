# taxonomy_vocabulary_static_reset()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 975–978 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L975-L978)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_vocabulary_static_reset($ids = NULL)
```

## Documentation

```text
Clear all static cache variables for vocabularies.

@param $ids
An array of ids to reset in entity controller cache.
```

## Code

```php
function taxonomy_vocabulary_static_reset($ids = NULL) {
  drupal_static_reset('taxonomy_vocabulary_get_names');
  entity_get_controller('taxonomy_vocabulary')->resetCache($ids);
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
