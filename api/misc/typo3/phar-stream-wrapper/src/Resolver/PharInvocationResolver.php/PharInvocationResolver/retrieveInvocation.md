# PharInvocationResolver::retrieveInvocation()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php`](../_file.md), lines 93–110 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php#L93-L110)
- **Class:** [PharInvocationResolver](../PharInvocationResolver.md)

## Signature

```php
private function retrieveInvocation($baseName, $flags)
```

## Documentation

```text
Retrieves PharInvocation, either existing in collection or created on demand
with resolving a potential alias name used in the according Phar archive.

@param string $baseName
@param int $flags
@return PharInvocation
```

## Code

```php
    private function retrieveInvocation($baseName, $flags)
    {
        $invocation = $this->findByBaseName($baseName);
        if ($invocation !== null) {
            return $invocation;
        }

        if ($flags & static::RESOLVE_ALIAS) {
            $reader = new Reader($baseName);
            $alias = $reader->resolveContainer()->getAlias();
        } else {
            $alias = '';
        }
        // add unconfirmed(!) new invocation to collection
        $invocation = new PharInvocation($baseName, $alias);
        Manager::instance()->getCollection()->collect($invocation);
        return $invocation;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php) · Licensed GPL-2.0-or-later (see LICENSE)._
