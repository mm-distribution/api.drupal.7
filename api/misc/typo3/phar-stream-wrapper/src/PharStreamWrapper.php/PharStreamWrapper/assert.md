# PharStreamWrapper::assert()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 406–421 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L406-L421)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
protected function assert($path, $command)
```

## Documentation

```text
@param string $path
@param string $command
```

## Code

```php
    protected function assert($path, $command)
    {
        if (Manager::instance()->assert($path, $command) === true) {
            $this->collectInvocation($path);
            return;
        }

        throw new Exception(
            sprintf(
                'Denied invocation of "%s" for command "%s"',
                $path,
                $command
            ),
            1535189880
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
