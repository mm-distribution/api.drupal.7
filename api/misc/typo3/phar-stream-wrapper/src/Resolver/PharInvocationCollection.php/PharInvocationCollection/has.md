# PharInvocationCollection::has()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php`](../_file.md), lines 31–34 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php#L31-L34)
- **Class:** [PharInvocationCollection](../PharInvocationCollection.md)

## Signature

```php
public function has(PharInvocation $invocation)
```

## Documentation

```text
@param PharInvocation $invocation
@return bool
```

## Code

```php
    public function has(PharInvocation $invocation)
    {
        return in_array($invocation, $this->invocations, true);
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php) · Licensed GPL-2.0-or-later (see LICENSE)._
