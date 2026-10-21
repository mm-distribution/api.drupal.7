# taxonomy_vocabulary_machine_name_load()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1381–1384 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1381-L1384)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_vocabulary_machine_name_load($name)
```

## Documentation

```text
Return the vocabulary object matching a vocabulary machine name.

@param $name
  The vocabulary's machine name.

@return
  The vocabulary object with all of its metadata, if exists, FALSE otherwise.
  Results are statically cached.

@see taxonomy_vocabulary_load()
```

## Code

```php
function taxonomy_vocabulary_machine_name_load($name) {
  $vocabularies = taxonomy_vocabulary_load_multiple(NULL, array('machine_name' => $name));
  return reset($vocabularies);
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
