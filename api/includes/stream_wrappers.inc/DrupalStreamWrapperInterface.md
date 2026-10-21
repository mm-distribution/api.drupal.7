# DrupalStreamWrapperInterface

- **Type:** Interface
- **File:** [`includes/stream_wrappers.inc`](_file.md), lines 126–220 · [local source](../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L126-L220)

## Signature

```php
interface DrupalStreamWrapperInterface extends StreamWrapperInterface
```

## Documentation

```text
Drupal stream wrapper extension.

Extend the StreamWrapperInterface with methods expected by Drupal stream
wrapper classes.
```

## Methods (derived index)

- [setUri()](DrupalStreamWrapperInterface/setUri.md) — Set the absolute stream resource URI.
- [getUri()](DrupalStreamWrapperInterface/getUri.md) — Returns the stream resource URI.
- [getExternalUrl()](DrupalStreamWrapperInterface/getExternalUrl.md) — Returns a web accessible URL for the resource.
- [getMimeType()](DrupalStreamWrapperInterface/getMimeType.md) — Returns the MIME type of the resource.
- [chmod()](DrupalStreamWrapperInterface/chmod.md) — Changes permissions of the resource.
- [realpath()](DrupalStreamWrapperInterface/realpath.md) — Returns canonical, absolute path of the resource.
- [dirname()](DrupalStreamWrapperInterface/dirname.md) — Gets the name of the directory from a given path.

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
