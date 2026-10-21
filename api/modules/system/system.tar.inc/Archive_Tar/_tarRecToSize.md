# Archive_Tar::_tarRecToSize()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 1835–1861 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L1835-L1861)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
private function _tarRecToSize($tar_size)
```

## Documentation

```text
Convert Tar record size to actual size

@param string $tar_size
@return size of tar record in bytes
```

## Code

```php
    private function _tarRecToSize($tar_size)
    {
        /*
         * First byte of size has a special meaning if bit 7 is set.
         *
         * Bit 7 indicates base-256 encoding if set.
         * Bit 6 is the sign bit.
         * Bits 5:0 are most significant value bits.
         */
        $ch = ord($tar_size[0]);
        if ($ch & 0x80) {
            // Full 12-bytes record is required.
            $rec_str = $tar_size . "\x00";

            $size = ($ch & 0x40) ? -1 : 0;
            $size = ($size << 6) | ($ch & 0x3f);

            for ($num_ch = 1; $num_ch < 12; ++$num_ch) {
                $size = ($size * 256) + ord($rec_str[$num_ch]);
            }

            return $size;

        } else {
            return OctDec(trim($tar_size));
        }
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
