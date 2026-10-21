# language_default()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3176–3179 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3176-L3179)

## Signature

```php
function language_default($property = NULL)
```

## Documentation

```text
Returns the default language, as an object, or one of its properties.

@param $property
  (optional) The property of the language object to return.

@return
  Either the language object for the default language used on the site,
  or the property of that object named in the $property parameter.
```

## Code

```php
function language_default($property = NULL) {
  $language = variable_get('language_default', (object) array('language' => 'en', 'name' => 'English', 'native' => 'English', 'direction' => 0, 'enabled' => 1, 'plurals' => 0, 'formula' => '', 'domain' => '', 'prefix' => '', 'weight' => 0, 'javascript' => ''));
  return $property ? $language->$property : $language;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
