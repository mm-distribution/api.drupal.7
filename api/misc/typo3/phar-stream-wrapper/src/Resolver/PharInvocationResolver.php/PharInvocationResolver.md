# PharInvocationResolver

- **Type:** Class
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php`](_file.md), lines 20–249 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php#L20-L249)

## Signature

```php
class PharInvocationResolver implements Resolvable
```

## Documentation

_No docblock in source._

## Constants

### RESOLVE_REALPATH

```php
const RESOLVE_REALPATH = 1;
```

### RESOLVE_ALIAS

```php
const RESOLVE_ALIAS = 2;
```

### ASSERT_INTERNAL_INVOCATION

```php
const ASSERT_INTERNAL_INVOCATION = 32;
```

## Properties

### $invocationFunctionNames

```php
private $invocationFunctionNames = array(
        'include',
        'include_once',
        'require',
        'require_once'
    );
```

```text
@var string[]
```

### $baseNames

```php
private $baseNames = array();
```

```text
Contains resolved base names in order to reduce file IO.

@var string[]
```

## Methods (derived index)

- [resolve()](PharInvocationResolver/resolve.md) — Resolves PharInvocation value object (baseName and optional alias).
- [retrieveInvocation()](PharInvocationResolver/retrieveInvocation.md) — Retrieves PharInvocation, either existing in collection or created on demand with resolving a potential alias name used in the according Phar archive.
- [resolveBaseName()](PharInvocationResolver/resolveBaseName.md)
- [resolvePossibleAlias()](PharInvocationResolver/resolvePossibleAlias.md)
- [findByBaseName()](PharInvocationResolver/findByBaseName.md)
- [findInBaseNames()](PharInvocationResolver/findInBaseNames.md)
- [addBaseName()](PharInvocationResolver/addBaseName.md)
- [findByAlias()](PharInvocationResolver/findByAlias.md) — Finds confirmed(!) invocations by alias.

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php) · Licensed GPL-2.0-or-later (see LICENSE)._
