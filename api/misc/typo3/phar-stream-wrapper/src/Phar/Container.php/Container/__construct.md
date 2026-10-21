# Container::__construct()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Phar/Container.php`](../_file.md), lines 30–34 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Phar/Container.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Container.php#L30-L34)
- **Class:** [Container](../Container.md)

## Signature

```php
public function __construct(Stub $stub, Manifest $manifest)
```

## Documentation

```text
@param Stub $stub
@param Manifest $manifest
```

## Code

```php
    public function __construct(Stub $stub, Manifest $manifest)
    {
        $this->stub = $stub;
        $this->manifest = $manifest;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Phar/Container.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Container.php) · Licensed GPL-2.0-or-later (see LICENSE)._
