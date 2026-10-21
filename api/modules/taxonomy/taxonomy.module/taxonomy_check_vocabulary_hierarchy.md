# taxonomy_check_vocabulary_hierarchy()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 571–595 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L571-L595)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_check_vocabulary_hierarchy($vocabulary, $changed_term)
```

## Documentation

```text
Checks and updates the hierarchy flag of a vocabulary.

Checks the current parents of all terms in a vocabulary and updates the
vocabulary's hierarchy setting to the lowest possible level. If no term
has parent terms then the vocabulary will be given a hierarchy of 0.
If any term has a single parent then the vocabulary will be given a
hierarchy of 1. If any term has multiple parents then the vocabulary
will be given a hierarchy of 2.

@param $vocabulary
  A vocabulary object.
@param $changed_term
  An array of the term structure that was updated.

@return
  An integer that represents the level of the vocabulary's hierarchy.
```

## Code

```php
function taxonomy_check_vocabulary_hierarchy($vocabulary, $changed_term) {
  $tree = taxonomy_get_tree($vocabulary->vid);
  $hierarchy = 0;
  foreach ($tree as $term) {
    // Update the changed term with the new parent value before comparison.
    if ($term->tid == $changed_term['tid']) {
      $term = (object) $changed_term;
      $term->parents = $term->parent;
    }
    // Check this term's parent count.
    if (count($term->parents) > 1) {
      $hierarchy = 2;
      break;
    }
    elseif (count($term->parents) == 1 && !isset($term->parents[0])) {
      $hierarchy = 1;
    }
  }
  if ($hierarchy != $vocabulary->hierarchy) {
    $vocabulary->hierarchy = $hierarchy;
    taxonomy_vocabulary_save($vocabulary);
  }

  return $hierarchy;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
