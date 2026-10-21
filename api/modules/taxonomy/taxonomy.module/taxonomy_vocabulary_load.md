# taxonomy_vocabulary_load()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1364–1367 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1364-L1367)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_vocabulary_load($vid)
```

## Documentation

```text
Return the vocabulary object matching a vocabulary ID.

@param $vid
  The vocabulary's ID.

@return
  The vocabulary object with all of its metadata, if exists, FALSE otherwise.
  Results are statically cached.

@see taxonomy_vocabulary_machine_name_load()
```

## Code

```php
function taxonomy_vocabulary_load($vid) {
  $vocabularies = taxonomy_vocabulary_load_multiple(array($vid));
  return reset($vocabularies);
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
