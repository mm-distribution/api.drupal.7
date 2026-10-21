# locale_get_plural()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 785–823 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L785-L823)
- **Module/theme:** locale

## Signature

```php
function locale_get_plural($count, $langcode = NULL)
```

## Documentation

```text
Returns plural form index for a specific number.

The index is computed from the formula of this language.

@param $count
  Number to return plural for.
@param $langcode
  Optional language code to translate to a language other than
  what is used to display the page.

@return
  The numeric index of the plural variant to use for this $langcode and
  $count combination or -1 if the language was not found or does not have a
  plural formula.
```

## Code

```php
function locale_get_plural($count, $langcode = NULL) {
  global $language;

  // Used to locally cache the plural formulas for all languages.
  $plural_formulas = &drupal_static(__FUNCTION__, array());

  // Used to store precomputed plural indexes corresponding to numbers
  // individually for each language.
  $plural_indexes = &drupal_static(__FUNCTION__ . ':plurals', array());

  $langcode = $langcode ? $langcode : $language->language;

  if (!isset($plural_indexes[$langcode][$count])) {
    // Retrieve and statically cache the plural formulas for all languages.
    if (empty($plural_formulas)) {
      foreach (language_list() as $installed_language) {
        $plural_formulas[$installed_language->language] = $installed_language->formula;
      }
    }
    // If there is a plural formula for the language, evaluate it for the given
    // $count and statically cache the result for the combination of language
    // and count, since the result will always be identical.
    if (!empty($plural_formulas[$langcode])) {
      // $n is used inside the expression in the eval().
      $n = $count;
      $plural_indexes[$langcode][$count] = @eval('return intval(' . $plural_formulas[$langcode] . ');');
    }
    // In case there is no plural formula for English (no imported translation
    // for English), use a default formula.
    elseif ($langcode == 'en') {
      $plural_indexes[$langcode][$count] = (int) ($count != 1);
    }
    // Otherwise, return -1 (unknown).
    else {
      $plural_indexes[$langcode][$count] = -1;
    }
  }
  return $plural_indexes[$langcode][$count];
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
