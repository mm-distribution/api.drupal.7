# PharInvocation

- **Type:** Class
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php`](_file.md), lines 16–125 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php#L16-L125)

## Signature

```php
class PharInvocation
```

## Documentation

_No docblock in source._

## Properties

### $baseName

```php
private $baseName;
```

```text
@var string
```

### $alias

```php
private $alias;
```

```text
@var string
```

### $confirmed

```php
private $confirmed = false;
```

```text
@var bool
@see \TYPO3\PharStreamWrapper\PharStreamWrapper::collectInvocation()
```

### $variables

```php
private $variables;
```

```text
Arbitrary variables to be used by interceptors as registry
(e.g. in order to avoid duplicate processing and assertions)

@var array
```

## Methods (derived index)

- [__construct()](PharInvocation/__construct.md)
- [__toString()](PharInvocation/__toString.md)
- [getBaseName()](PharInvocation/getBaseName.md)
- [getAlias()](PharInvocation/getAlias.md)
- [isConfirmed()](PharInvocation/isConfirmed.md)
- [confirm()](PharInvocation/confirm.md)
- [getVariable()](PharInvocation/getVariable.md)
- [setVariable()](PharInvocation/setVariable.md)
- [equals()](PharInvocation/equals.md)

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php) · Licensed GPL-2.0-or-later (see LICENSE)._
