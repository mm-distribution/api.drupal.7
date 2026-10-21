# DrupalRequestSanitizer

- **Type:** Class
- **File:** [`includes/request-sanitizer.inc`](_file.md), lines 11–114 · [local source](../../../source/includes/request-sanitizer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/request-sanitizer.inc#L11-L114)

## Signature

```php
class DrupalRequestSanitizer
```

## Documentation

```text
Sanitizes user input from the request.
```

## Properties

### $sanitized

```php
protected static $sanitized = FALSE;
```

```text
Tracks whether the request was already sanitized.
```

## Methods (derived index)

- [sanitize()](DrupalRequestSanitizer/sanitize.md) — Modifies the request to strip dangerous keys from user input.
- [cleanDestination()](DrupalRequestSanitizer/cleanDestination.md) — Removes the destination if it is dangerous.
- [stripDangerousValues()](DrupalRequestSanitizer/stripDangerousValues.md) — Strips dangerous keys from the provided input.

---
_Drupal 7.103 · [includes/request-sanitizer.inc](https://github.com/drupal/drupal/blob/7.103/includes/request-sanitizer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
