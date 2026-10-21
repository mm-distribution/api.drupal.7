# PharInvocationCollection::collect()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php`](../_file.md), lines 41–59 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php#L41-L59)
- **Class:** [PharInvocationCollection](../PharInvocationCollection.md)

## Signature

```php
public function collect(PharInvocation $invocation, $flags = null)
```

## Documentation

```text
@param PharInvocation $invocation
@param null|int $flags
@return bool
```

## Code

```php
    public function collect(PharInvocation $invocation, $flags = null)
    {
        if ($flags === null) {
            $flags = static::UNIQUE_INVOCATION | static::DUPLICATE_ALIAS_WARNING;
        }
        if ($invocation->getBaseName() === ''
            || $invocation->getAlias() === ''
            || !$this->assertUniqueBaseName($invocation, $flags)
            || !$this->assertUniqueInvocation($invocation, $flags)
        ) {
            return false;
        }
        if ($flags & static::DUPLICATE_ALIAS_WARNING) {
            $this->triggerDuplicateAliasWarning($invocation);
        }

        $this->invocations[] = $invocation;
        return true;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php) · Licensed GPL-2.0-or-later (see LICENSE)._
