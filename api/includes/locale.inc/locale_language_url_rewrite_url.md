# locale_language_url_rewrite_url()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 411–490 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L411-L490)
- **Topics:** [locale-languages-negotiation](../../topics/locale-languages-negotiation.md)

## Signature

```php
function locale_language_url_rewrite_url(&$path, &$options)
```

## Documentation

```text
Rewrite URLs for the URL language provider.
```

## Code

```php
function locale_language_url_rewrite_url(&$path, &$options) {
  static $drupal_static_fast;
  if (!isset($drupal_static_fast)) {
    $drupal_static_fast['languages'] = &drupal_static(__FUNCTION__);
  }
  $languages = &$drupal_static_fast['languages'];

  if (!isset($languages)) {
    $languages = language_list('enabled');
    $languages = array_flip(array_keys($languages[1]));
  }

  // Language can be passed as an option, or we go for current URL language.
  if (!isset($options['language'])) {
    global $language_url;
    $options['language'] = $language_url;
  }
  // We allow only enabled languages here.
  elseif (!isset($languages[$options['language']->language])) {
    unset($options['language']);
    return;
  }

  if (isset($options['language'])) {
    switch (variable_get('locale_language_negotiation_url_part', LOCALE_LANGUAGE_NEGOTIATION_URL_PREFIX)) {
      case LOCALE_LANGUAGE_NEGOTIATION_URL_DOMAIN:
        if ($options['language']->domain) {
          // Save the original base URL. If it contains a port, we need to
          // retain it below.
          if (!empty($options['base_url'])) {
            // The colon in the URL scheme messes up the port checking below.
            $normalized_base_url = str_replace(array('https://', 'http://'), '', $options['base_url']);
          }

          // Ask for an absolute URL with our modified base_url.
          global $is_https;
          $url_scheme = ($is_https) ? 'https://' : 'http://';
          $options['absolute'] = TRUE;

          // Take the domain without ports or protocols so we can apply the
          // protocol needed. The setting might include a protocol.
          // This is changed in Drupal 8 but we need to keep backwards
          // compatibility for Drupal 7.
          $host = 'http://' . str_replace(array('http://', 'https://'), '', $options['language']->domain);
          $host = parse_url($host, PHP_URL_HOST);

          // Apply the appropriate protocol to the URL.
          $options['base_url'] = $url_scheme . $host;

          // In case either the original base URL or the HTTP host contains a
          // port, retain it.
          $http_host = $_SERVER['HTTP_HOST'];
          if (isset($normalized_base_url) && strpos($normalized_base_url, ':') !== FALSE) {
            list($host, $port) = explode(':', $normalized_base_url);
            $options['base_url'] .= ':' . $port;
          }
          elseif (strpos($http_host, ':') !== FALSE) {
            list($host, $port) = explode(':', $http_host);
            $options['base_url'] .= ':' . $port;
          }

          if (isset($options['https']) && variable_get('https', FALSE)) {
            if ($options['https'] === TRUE) {
              $options['base_url'] = str_replace('http://', 'https://', $options['base_url']);
            }
            elseif ($options['https'] === FALSE) {
              $options['base_url'] = str_replace('https://', 'http://', $options['base_url']);
            }
          }
        }
        break;

      case LOCALE_LANGUAGE_NEGOTIATION_URL_PREFIX:
        if (!empty($options['language']->prefix)) {
          $options['prefix'] = $options['language']->prefix . '/';
        }
        break;
    }
  }
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
