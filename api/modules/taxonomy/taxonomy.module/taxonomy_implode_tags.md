# taxonomy_implode_tags()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1416–1434 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1416-L1434)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_implode_tags($tags, $vid = NULL)
```

## Documentation

```text
Implodes a list of tags of a certain vocabulary into a string.

@see drupal_explode_tags()
```

## Code

```php
function taxonomy_implode_tags($tags, $vid = NULL) {
  $typed_tags = array();
  foreach ($tags as $tag) {
    // Extract terms belonging to the vocabulary in question.
    if (!isset($vid) || $tag->vid == $vid) {
      // Make sure we have a completed loaded taxonomy term.
      if (isset($tag->name)) {
        // Commas and quotes in tag names are special cases, so encode 'em.
        if (strpos($tag->name, ',') !== FALSE || strpos($tag->name, '"') !== FALSE) {
          $typed_tags[] = '"' . str_replace('"', '""', $tag->name) . '"';
        }
        else {
          $typed_tags[] = $tag->name;
        }
      }
    }
  }
  return implode(', ', $typed_tags);
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
