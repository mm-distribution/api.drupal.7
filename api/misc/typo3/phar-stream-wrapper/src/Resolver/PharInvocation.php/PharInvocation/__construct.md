# PharInvocation::__construct()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php`](../_file.md), lines 46–56 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php#L46-L56)
- **Class:** [PharInvocation](../PharInvocation.md)

## Signature

```php
public function __construct($baseName, $alias = '')
```

## Documentation

```text
@param string $baseName
@param string $alias
```

## Code

```php
    public function __construct($baseName, $alias = '')
    {
        if ($baseName === '') {
            throw new Exception(
                'Base-name cannot be empty',
                1551283689
            );
        }
        $this->baseName = $baseName;
        $this->alias = $alias;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php) · Licensed GPL-2.0-or-later (see LICENSE)._
