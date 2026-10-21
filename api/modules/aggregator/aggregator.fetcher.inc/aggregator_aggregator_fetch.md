# aggregator_aggregator_fetch()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.fetcher.inc`](_file.md), lines 21–61 · [local source](../../../../source/modules/aggregator/aggregator.fetcher.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.fetcher.inc#L21-L61)
- **Module/theme:** aggregator
- **Implements:** [hook_aggregator_fetch()](../aggregator.api.php/hook_aggregator_fetch.md)

## Signature

```php
function aggregator_aggregator_fetch($feed)
```

## Documentation

```text
Implements hook_aggregator_fetch().
```

## Code

```php
function aggregator_aggregator_fetch($feed) {
  $feed->source_string = FALSE;

  // Generate conditional GET headers.
  $headers = array();
  if ($feed->etag) {
    $headers['If-None-Match'] = $feed->etag;
  }
  if ($feed->modified) {
    $headers['If-Modified-Since'] = gmdate(DATE_RFC7231, $feed->modified);
  }

  // Request feed.
  $result = drupal_http_request($feed->url, array('headers' => $headers));

  // Process HTTP response code.
  switch ($result->code) {
    case 304:
      break;
    case 301:
      $feed->url = $result->redirect_url;
      // Do not break here.
    case 200:
    case 302:
    case 307:
      if (!isset($result->data)) {
        $result->data = '';
      }
      if (!isset($result->headers)) {
        $result->headers = array();
      }
      $feed->source_string = $result->data;
      $feed->http_headers = $result->headers;
      break;
    default:
      watchdog('aggregator', 'The feed from %site seems to be broken, due to "%error".', array('%site' => $feed->title, '%error' => $result->code . ' ' . $result->error), WATCHDOG_WARNING);
      drupal_set_message(t('The feed from %site seems to be broken, because of error "%error".', array('%site' => $feed->title, '%error' => $result->code . ' ' . $result->error)));
  }

  return $feed->source_string === FALSE ? FALSE : TRUE;
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.fetcher.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.fetcher.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
