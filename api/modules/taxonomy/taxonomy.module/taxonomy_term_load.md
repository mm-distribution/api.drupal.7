# taxonomy_term_load()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1396–1402 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1396-L1402)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_term_load($tid)
```

## Documentation

```text
Return the term object matching a term ID.

@param $tid
  A term's ID

@return
  A taxonomy term object, or FALSE if the term was not found. Results are
  statically cached.
```

## Code

```php
function taxonomy_term_load($tid) {
  if (!is_numeric($tid)) {
    return FALSE;
  }
  $term = taxonomy_term_load_multiple(array($tid), array());
  return $term ? $term[$tid] : FALSE;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
