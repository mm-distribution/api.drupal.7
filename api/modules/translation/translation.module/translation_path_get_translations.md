# translation_path_get_translations()

- **Type:** Function
- **File:** [`modules/translation/translation.module`](_file.md), lines 527–536 · [local source](../../../../source/modules/translation/translation.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module#L527-L536)
- **Module/theme:** translation

## Signature

```php
function translation_path_get_translations($path)
```

## Documentation

```text
Returns the paths of all translations of a node, based on its Drupal path.

@param $path
  A Drupal path, for example node/432.

@return
  An array of paths of translations of the node accessible to the current
  user, keyed with language codes.
```

## Code

```php
function translation_path_get_translations($path) {
  $paths = array();
  // Check for a node related path, and for its translations.
  if ((preg_match("!^node/(\d+)(/.+|)$!", $path, $matches)) && ($node = node_load((int) $matches[1])) && !empty($node->tnid)) {
    foreach (translation_node_get_translations($node->tnid) as $language => $translation_node) {
      $paths[$language] = 'node/' . $translation_node->nid . $matches[2];
    }
  }
  return $paths;
}
```

---
_Drupal 7.103 · [modules/translation/translation.module](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module) · Licensed GPL-2.0-or-later (see LICENSE)._
