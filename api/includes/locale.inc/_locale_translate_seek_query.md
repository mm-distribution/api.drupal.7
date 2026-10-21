# _locale_translate_seek_query()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 1988–2000 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L1988-L2000)
- **Topics:** [locale-api-seek](../../topics/locale-api-seek.md)

## Signature

```php
function _locale_translate_seek_query()
```

## Documentation

```text
Build array out of search criteria specified in request variables
```

## Code

```php
function _locale_translate_seek_query() {
  $query = &drupal_static(__FUNCTION__);
  if (!isset($query)) {
    $query = array();
    $fields = array('string', 'language', 'translation', 'group');
    foreach ($fields as $field) {
      if (isset($_SESSION['locale_translation_filter'][$field])) {
        $query[$field] = $_SESSION['locale_translation_filter'][$field];
      }
    }
  }
  return $query;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
