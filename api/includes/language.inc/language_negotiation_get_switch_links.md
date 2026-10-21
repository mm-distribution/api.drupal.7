# language_negotiation_get_switch_links()

- **Type:** Function
- **File:** [`includes/language.inc`](_file.md), lines 279–313 · [local source](../../../source/includes/language.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/language.inc#L279-L313)
- **Topics:** [language_negotiation](../../topics/language_negotiation.md)

## Signature

```php
function language_negotiation_get_switch_links($type, $path)
```

## Documentation

```text
Returns the language switch links for the given language.

@param $type
  The language negotiation type.
@param $path
  The internal path the switch links will be relative to.

@return
  A keyed array of links ready to be themed.
```

## Code

```php
function language_negotiation_get_switch_links($type, $path) {
  $links = FALSE;
  $negotiation = variable_get("language_negotiation_$type", array());

  // Only get the languages if we have more than one.
  if (count(language_list()) >= 2) {
    $language = language_initialize($type);
  }

  foreach ($negotiation as $id => $provider) {
    if (isset($provider['callbacks']['switcher'])) {
      if (isset($provider['file'])) {
        require_once DRUPAL_ROOT . '/' . $provider['file'];
      }

      $callback = $provider['callbacks']['switcher'];
      $result = $callback($type, $path);

      // Add support for WCAG 2.0's Language of Parts to add language identifiers.
      // http://www.w3.org/TR/UNDERSTANDING-WCAG20/meaning-other-lang-id.html
      foreach ($result as $langcode => $link) {
        $result[$langcode]['attributes']['xml:lang'] = $langcode;
      }

      if (!empty($result)) {
        // Allow modules to provide translations for specific links.
        drupal_alter('language_switch_links', $result, $type, $path);
        $links = (object) array('links' => $result, 'provider' => $id);
        break;
      }
    }
  }

  return $links;
}
```

---
_Drupal 7.103 · [includes/language.inc](https://github.com/drupal/drupal/blob/7.103/includes/language.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
