# PharInvocationResolver::resolve()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php`](../_file.md), lines 59–83 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php#L59-L83)
- **Class:** [PharInvocationResolver](../PharInvocationResolver.md)

## Signature

```php
public function resolve($path, $flags = null)
```

## Documentation

```text
Resolves PharInvocation value object (baseName and optional alias).

Phar aliases are intended to be used only inside Phar archives, however
PharStreamWrapper needs this information exposed outside of Phar as well
It is possible that same alias is used for different $baseName values.
That's why PharInvocationCollection behaves like a stack when resolving
base-name for a given alias. On the other hand it is not possible that
one $baseName is referring to multiple aliases.
@see https://secure.php.net/manual/en/phar.setalias.php
@see https://secure.php.net/manual/en/phar.mapphar.php

@param string $path
@param int|null $flags
@return null|PharInvocation
```

## Code

```php
    public function resolve($path, $flags = null)
    {
        $hasPharPrefix = Helper::hasPharPrefix($path);
        if ($flags === null) {
            $flags = static::RESOLVE_REALPATH | static::RESOLVE_ALIAS;
        }

        if ($hasPharPrefix && $flags & static::RESOLVE_ALIAS) {
            $invocation = $this->findByAlias($path);
            if ($invocation !== null) {
                return $invocation;
            }
        }

        $baseName = $this->resolveBaseName($path, $flags);
        if ($baseName === null) {
            return null;
        }

        if ($flags & static::RESOLVE_REALPATH) {
            $baseName = $this->baseNames[$baseName];
        }

        return $this->retrieveInvocation($baseName, $flags);
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php) · Licensed GPL-2.0-or-later (see LICENSE)._
