# _locale_export_get_strings()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 1652–1678 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L1652-L1678)
- **Topics:** [locale-api-import-export](../../topics/locale-api-import-export.md)

## Signature

```php
function _locale_export_get_strings($language = NULL, $group = 'default')
```

## Documentation

```text
Generates a structured array of all strings with translations in
$language, if given. This array can be used to generate an export
of the string in the database.

@param $language
  Language object to generate the output for, or NULL if generating
  translation template.
@param $group
  Text group to export PO file from (eg. 'default' for interface
  translations).
```

## Code

```php
function _locale_export_get_strings($language = NULL, $group = 'default') {
  if (isset($language)) {
    $result = db_query("SELECT s.lid, s.source, s.context, s.location, t.translation, t.plid, t.plural FROM {locales_source} s LEFT JOIN {locales_target} t ON s.lid = t.lid AND t.language = :language WHERE s.textgroup = :textgroup ORDER BY t.plid, t.plural", array(':language' => $language->language, ':textgroup' => $group));
  }
  else {
    $result = db_query("SELECT s.lid, s.source, s.context, s.location, t.plid, t.plural FROM {locales_source} s LEFT JOIN {locales_target} t ON s.lid = t.lid WHERE s.textgroup = :textgroup ORDER BY t.plid, t.plural", array(':textgroup' => $group));
  }
  $strings = array();
  foreach ($result as $child) {
    $string = array(
      'comment'     => $child->location,
      'source'      => $child->source,
      'context'     => $child->context,
      'translation' => isset($child->translation) ? $child->translation : '',
    );
    if ($child->plid) {
      // Has a parent lid. Since we process in the order of plids,
      // we already have the parent in the array, so we can add the
      // lid to the next plural version to it. This builds a linked
      // list of plurals.
      $string['child'] = TRUE;
      $strings[$child->plid]['plural'] = $child->lid;
    }
    $strings[$child->lid] = $string;
  }
  return $strings;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
