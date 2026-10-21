# language_url_split_prefix()

- **Type:** Function
- **File:** [`includes/language.inc`](_file.md), lines 530–543 · [local source](../../../source/includes/language.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/language.inc#L530-L543)
- **Topics:** [language_negotiation](../../topics/language_negotiation.md)

## Signature

```php
function language_url_split_prefix($path, $languages)
```

## Documentation

```text
Splits the given path into prefix and actual path.

Parse the given path and return the language object identified by the prefix
and the actual path.

@param $path
  The path to split.
@param $languages
  An array of valid languages.

@return
  An array composed of:
   - A language object corresponding to the identified prefix on success,
     FALSE otherwise.
   - The path without the prefix on success, the given path otherwise.
```

## Code

```php
function language_url_split_prefix($path, $languages) {
  $args = empty($path) ? array() : explode('/', $path);
  $prefix = array_shift($args);

  // Search prefix within enabled languages.
  foreach ($languages as $language) {
    if (!empty($language->prefix) && $language->prefix == $prefix) {
      // Rebuild $path with the language removed.
      return array($language, implode('/', $args));
    }
  }

  return array(FALSE, $path);
}
```

---
_Drupal 7.103 · [includes/language.inc](https://github.com/drupal/drupal/blob/7.103/includes/language.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
