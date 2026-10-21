# taxonomy_get_term_by_name()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1228–1241 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1228-L1241)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_get_term_by_name($name, $vocabulary = NULL)
```

## Documentation

```text
Try to map a string to an existing term, as for glossary use.

Provides a case-insensitive and trimmed mapping, to maximize the
likelihood of a successful match.

@param $name
  Name of the term to search for.
@param $vocabulary
  (optional) Vocabulary machine name to limit the search. Defaults to NULL.

@return
  An array of matching term objects.
```

## Code

```php
function taxonomy_get_term_by_name($name, $vocabulary = NULL) {
  $conditions = array('name' => trim($name));
  if (isset($vocabulary)) {
    $vocabularies = taxonomy_vocabulary_get_names();
    if (isset($vocabularies[$vocabulary])) {
      $conditions['vid'] = $vocabularies[$vocabulary]->vid;
    }
    else {
      // Return an empty array when filtering by a non-existing vocabulary.
      return array();
    }
  }
  return taxonomy_term_load_multiple(array(), $conditions);
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
