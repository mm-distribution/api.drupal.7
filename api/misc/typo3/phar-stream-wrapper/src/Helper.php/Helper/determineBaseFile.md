# Helper::determineBaseFile()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Helper.php`](../_file.md), lines 49–62 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Helper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php#L49-L62)
- **Class:** [Helper](../Helper.md)

## Signature

```php
public static function determineBaseFile($path)
```

## Documentation

```text
Determines base file that can be accessed using the regular file system.
For e.g. "phar:///home/user/bundle.phar/content.txt" that would result
into "/home/user/bundle.phar".

@param string $path
@return string|null
```

## Code

```php
    public static function determineBaseFile($path)
    {
        $parts = explode('/', static::normalizePath($path));

        while (count($parts)) {
            $currentPath = implode('/', $parts);
            if (@is_file($currentPath) && realpath($currentPath) !== false) {
                return $currentPath;
            }
            array_pop($parts);
        }

        return null;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Helper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
