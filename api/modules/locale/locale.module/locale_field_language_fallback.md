# locale_field_language_fallback()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 496–520 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L496-L520)
- **Module/theme:** locale

## Signature

```php
function locale_field_language_fallback(&$display_language, $entity, $langcode)
```

## Documentation

```text
Applies language fallback rules to the fields attached to the given entity.

Core language fallback rules simply check if fields have a field translation
for the requested language code. If so the requested language is returned,
otherwise all the fallback candidates are inspected to see if there is a
field translation available in another language.
By default this is called by locale_field_language_alter(), but this
behavior can be disabled by setting the 'locale_field_language_fallback'
variable to FALSE.

@param $display_language
  A reference to an array of language codes keyed by field name.
@param $entity
  The entity to be displayed.
@param $langcode
  The language code $entity has to be displayed in.
```

## Code

```php
function locale_field_language_fallback(&$display_language, $entity, $langcode) {
  // Lazily init fallback candidates to avoid unnecessary calls.
  $fallback_candidates = NULL;
  $field_languages = array();

  foreach ($display_language as $field_name => $field_language) {
    // If the requested language is defined for the current field use it,
    // otherwise search for a fallback value among the fallback candidates.
    if (isset($entity->{$field_name}[$langcode])) {
      $display_language[$field_name] = $langcode;
    }
    elseif (!empty($entity->{$field_name})) {
      if (!isset($fallback_candidates)) {
        require_once DRUPAL_ROOT . '/includes/language.inc';
        $fallback_candidates = language_fallback_get_candidates();
      }
      foreach ($fallback_candidates as $fallback_language) {
        if (isset($entity->{$field_name}[$fallback_language])) {
          $display_language[$field_name] = $fallback_language;
          break;
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
