# locale_language_from_url()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 264–305 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L264-L305)
- **Topics:** [locale-languages-negotiation](../../topics/locale-languages-negotiation.md)

## Signature

```php
function locale_language_from_url($languages)
```

## Documentation

```text
Identify language via URL prefix or domain.

@param $languages
  An array of valid language objects.

@return
  A valid language code on success, FALSE otherwise.
```

## Code

```php
function locale_language_from_url($languages) {
  $language_url = FALSE;

  if (!language_negotiation_get_any(LOCALE_LANGUAGE_NEGOTIATION_URL)) {
    return $language_url;
  }

  switch (variable_get('locale_language_negotiation_url_part', LOCALE_LANGUAGE_NEGOTIATION_URL_PREFIX)) {
    case LOCALE_LANGUAGE_NEGOTIATION_URL_PREFIX:
      // $_GET['q'] might not be available at this time, because
      // path initialization runs after the language bootstrap phase.
      list($language, $_GET['q']) = language_url_split_prefix(isset($_GET['q']) ? $_GET['q'] : NULL, $languages);
      if ($language !== FALSE) {
        $language_url = $language->language;
      }
      break;

    case LOCALE_LANGUAGE_NEGOTIATION_URL_DOMAIN:
      // Get only the host, not the port.
      $http_host= $_SERVER['HTTP_HOST'];
      if (strpos($http_host, ':') !== FALSE) {
        $http_host_tmp = explode(':', $http_host);
        $http_host = current($http_host_tmp);
      }
      foreach ($languages as $language) {
        // Skip check if the language doesn't have a domain.
        if ($language->domain) {
          // Only compare the domains not the protocols or ports.
          // Remove protocol and add http:// so parse_url works
          $host = 'http://' . str_replace(array('http://', 'https://'), '', $language->domain);
          $host = parse_url($host, PHP_URL_HOST);
          if ($http_host == $host) {
            $language_url = $language->language;
            break;
          }
        }
      }
      break;
  }

  return $language_url;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
