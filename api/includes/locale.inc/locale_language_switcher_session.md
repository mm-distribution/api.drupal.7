# locale_language_switcher_session()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 377–406 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L377-L406)
- **Topics:** [locale-languages-negotiation](../../topics/locale-languages-negotiation.md)

## Signature

```php
function locale_language_switcher_session($type, $path)
```

## Documentation

```text
Return the session language switcher block.
```

## Code

```php
function locale_language_switcher_session($type, $path) {
  drupal_add_css(drupal_get_path('module', 'locale') . '/locale.css');

  $param = variable_get('locale_language_negotiation_session_param', 'language');
  $language_query = isset($_SESSION[$param]) ? $_SESSION[$param] : $GLOBALS[$type]->language;

  $languages = language_list('enabled');
  $links = array();

  $query = $_GET;
  unset($query['q']);

  foreach ($languages[1] as $language) {
    $langcode = $language->language;
    $links[$langcode] = array(
      'href'       => $path,
      'title'      => $language->native,
      'attributes' => array('class' => array('language-link')),
      'query'      => $query,
    );
    if ($language_query != $langcode) {
      $links[$langcode]['query'][$param] = $langcode;
    }
    else {
      $links[$langcode]['attributes']['class'][] = 'session-active';
    }
  }

  return $links;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
