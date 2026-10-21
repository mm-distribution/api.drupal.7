# ThemeRegistry

- **Type:** Class
- **File:** [`includes/theme.inc`](_file.md), lines 365–465 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L365-L465)

## Signature

```php
class ThemeRegistry Extends DrupalCacheArray
```

## Documentation

```text
Builds the run-time theme registry.

Extends DrupalCacheArray to allow the theme registry to be accessed as a
complete registry, while internally caching only the parts of the registry
that are actually in use on the site. On cache misses the complete
theme registry is loaded and used to update the run-time cache.
```

## Properties

### $persistable

```php
protected $persistable;
```

```text
Whether the partial registry can be persisted to the cache.

This is only allowed if all modules and the request method is GET. theme()
should be very rarely called on POST requests and this avoids polluting
the runtime cache.
```

### $completeRegistry

```php
protected $completeRegistry;
```

```text
The complete theme registry array.
```

## Methods (derived index)

- [__construct()](ThemeRegistry/__construct.md)
- [initializeRegistry()](ThemeRegistry/initializeRegistry.md) — Initializes the full theme registry.
- [offsetExists()](ThemeRegistry/offsetExists.md)
- [offsetGet()](ThemeRegistry/offsetGet.md)
- [resolveCacheMiss()](ThemeRegistry/resolveCacheMiss.md)
- [set()](ThemeRegistry/set.md)

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
