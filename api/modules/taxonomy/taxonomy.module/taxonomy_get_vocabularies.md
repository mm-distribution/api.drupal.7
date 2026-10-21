# taxonomy_get_vocabularies()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 986–988 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L986-L988)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_get_vocabularies()
```

## Documentation

```text
Return an array of all vocabulary objects.

@return
  An array of all vocabulary objects, indexed by vid.
```

## Code

```php
function taxonomy_get_vocabularies() {
  return taxonomy_vocabulary_load_multiple(FALSE, array());
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
