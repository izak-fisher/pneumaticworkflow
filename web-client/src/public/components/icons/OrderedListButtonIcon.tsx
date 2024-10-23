/* eslint-disable */
/* prettier-ignore */
import * as React from 'react';

export type TOrderedListButtonIconProps = React.SVGAttributes<SVGElement>;

export function OrderedListButtonIcon({ fill = 'currentColor' }: TOrderedListButtonIconProps) {
  return (
    <svg width="24" height="24" viewBox="0 0 24 24" fill={fill} xmlns="http://www.w3.org/2000/svg">
      <path d="M8 4H21V6H8V4ZM5 3V6H6V7H3V6H4V4H3V3H5ZM3 14V11.5H5V11H3V10H6V12.5H4V13H6V14H3ZM5 19.5H3V18.5H5V18H3V17H6V21H3V20H5V19.5ZM8 11H21V13H8V11ZM8 18H21V20H8V18Z" />
    </svg>
  );
}