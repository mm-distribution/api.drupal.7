# PharInvocationCollection

- **Type:** Class
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php`](_file.md), lines 16–156 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php#L16-L156)

## Signature

```php
class PharInvocationCollection implements Collectable
```

## Documentation

_No docblock in source._

## Constants

### UNIQUE_INVOCATION

```php
const UNIQUE_INVOCATION = 1;
```

### UNIQUE_BASE_NAME

```php
const UNIQUE_BASE_NAME = 2;
```

### DUPLICATE_ALIAS_WARNING

```php
const DUPLICATE_ALIAS_WARNING = 32;
```

## Properties

### $invocations

```php
private $invocations = array();
```

```text
@var PharInvocation[]
```

## Methods (derived index)

- [has()](PharInvocationCollection/has.md)
- [collect()](PharInvocationCollection/collect.md)
- [findByCallback()](PharInvocationCollection/findByCallback.md)
- [assertUniqueBaseName()](PharInvocationCollection/assertUniqueBaseName.md) — Asserts that base-name is unique. This disallows having multiple invocations for same base-name but having different alias names.
- [assertUniqueInvocation()](PharInvocationCollection/assertUniqueInvocation.md) — Asserts that combination of base-name and alias is unique. This allows having multiple invocations for same base-name but having different alias names (for whatever reason).
- [triggerDuplicateAliasWarning()](PharInvocationCollection/triggerDuplicateAliasWarning.md) — Triggers warning for invocations with same alias and same confirmation state.
- [getInvocations()](PharInvocationCollection/getInvocations.md)

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php) · Licensed GPL-2.0-or-later (see LICENSE)._
