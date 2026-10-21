# drupal_strip_dangerous_protocols()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1448–1477 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1448-L1477)
- **Topics:** [sanitization](../../topics/sanitization.md)

## Signature

```php
function drupal_strip_dangerous_protocols($uri)
```

## Documentation

```text
Strips dangerous protocols (e.g. 'javascript:') from a URI.

This function must be called for all URIs within user-entered input prior
to being output to an HTML attribute value. It is often called as part of
check_url() or filter_xss(), but those functions return an HTML-encoded
string, so this function can be called independently when the output needs to
be a plain-text string for passing to t(), l(), drupal_attributes(), or
another function that will call check_plain() separately.

@param $uri
  A plain-text URI that might contain dangerous protocols.

@return
  A plain-text URI stripped of dangerous protocols. As with all plain-text
  strings, this return value must not be output to an HTML page without
  check_plain() being called on it. However, it can be passed to functions
  expecting plain-text strings.

@see check_url()
```

## Code

```php
function drupal_strip_dangerous_protocols($uri) {
  static $allowed_protocols;

  if (!isset($allowed_protocols)) {
    $allowed_protocols = array_flip(variable_get('filter_allowed_protocols', array('ftp', 'http', 'https', 'irc', 'mailto', 'news', 'nntp', 'rtsp', 'sftp', 'ssh', 'tel', 'telnet', 'webcal')));
  }

  // Iteratively remove any invalid protocol found.
  do {
    $before = $uri;
    $colonpos = strpos($uri, ':');
    if ($colonpos > 0) {
      // We found a colon, possibly a protocol. Verify.
      $protocol = substr($uri, 0, $colonpos);
      // If a colon is preceded by a slash, question mark or hash, it cannot
      // possibly be part of the URL scheme. This must be a relative URL, which
      // inherits the (safe) protocol of the base document.
      if (preg_match('![/?#]!', $protocol)) {
        break;
      }
      // Check if this is a disallowed protocol. Per RFC2616, section 3.2.3
      // (URI Comparison) scheme comparison must be case-insensitive.
      if (!isset($allowed_protocols[strtolower($protocol)])) {
        $uri = substr($uri, $colonpos + 1);
      }
    }
  } while ($before != $uri);

  return $uri;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
