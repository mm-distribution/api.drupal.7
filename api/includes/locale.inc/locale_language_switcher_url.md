# locale_language_switcher_url()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 358–372 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L358-L372)
- **Topics:** [locale-languages-negotiation](../../topics/locale-languages-negotiation.md)

## Signature

```php
function locale_language_switcher_url($type, $path)
```

## Documentation

```text
Return the URL language switcher block. Translation links may be provided by
other modules.
```

## Code

```php
function locale_language_switcher_url($type, $path) {
  $languages = language_list('enabled');
  $links = array();

  foreach ($languages[1] as $language) {
    $links[$language->language] = array(
      'href'       => $path,
      'title'      => $language->native,
      'language'   => $language,
      'attributes' => array('class' => array('language-link')),
    );
  }

  return $links;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
