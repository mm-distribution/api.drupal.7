# Archive_Tar::add()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 368–371 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L368-L371)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function add($p_filelist)
```

## Documentation

```text
This method add the files / directories that are listed in $p_filelist in
the archive. If the archive does not exist it is created.
The method return false and a PEAR error text.
The files and directories listed are only added at the end of the archive,
even if a file with the same name is already archived.
See also createModify() method for more details.

@param array $p_filelist An array of filenames and directory names, or a
             single string with names separated by a single
             blank space.

@return bool true on success, false on error.
@see    createModify()
@access public
```

## Code

```php
    public function add($p_filelist)
    {
        return $this->addModify($p_filelist, '', '');
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
