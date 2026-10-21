# DrupalStreamWrapperInterface::getExternalUrl()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 157–157 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L157)
- **Class:** [DrupalStreamWrapperInterface](../DrupalStreamWrapperInterface.md)

## Signature

```php
public function getExternalUrl();
```

## Documentation

```text
Returns a web accessible URL for the resource.

This function should return a URL that can be embedded in a web page
and accessed from a browser. For example, the external URL of
"youtube://xIpLd0WQKCY" might be
"http://www.youtube.com/watch?v=xIpLd0WQKCY".

@return
  Returns a string containing a web accessible URL for the resource.
```

## Code

```php
  public function getExternalUrl();
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
