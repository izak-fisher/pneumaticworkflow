/* eslint-disable */
/* prettier-ignore */
import * as React from 'react';

export type TUnionIconProps = React.SVGAttributes<SVGElement>;

export function UnionIcon({ fill = 'currentColor', ...rest }: TUnionIconProps) {
  return (
    <svg width="20" height="20" viewBox="0 0 20 20" fill={fill} xmlns="http://www.w3.org/2000/svg" {...rest}>
      <path fillRule="evenodd" clipRule="evenodd" d="M11 2C12.5977 2 13.9037 3.24892 13.9949 4.82373L14 5V6H15C16.5977 6 17.9037 7.24892 17.9949 8.82373L18 9V15C18 16.5977 16.7511 17.9037 15.1763 17.9949L15 18H9C7.40232 18 6.09634 16.7511 6.00509 15.1763L6 15V14H5C3.40232 14 2.09634 12.7511 2.00509 11.1763L2 11V5C2 3.40232 3.24892 2.09634 4.82373 2.00509L5 2H11ZM15 8H14V11C14 12.5977 12.7511 13.9037 11.1763 13.9949L11 14H8V15C8 15.5128 8.38604 15.9355 8.88338 15.9933L9 16H15C15.5128 16 15.9355 15.614 15.9933 15.1166L16 15V9C16 8.48716 15.614 8.06449 15.1166 8.00673L15 8ZM11 4H5C4.48716 4 4.06449 4.38604 4.00673 4.88338L4 5V11C4 11.5128 4.38604 11.9355 4.88338 11.9933L5 12H6V9C6 7.40232 7.24892 6.09634 8.82373 6.00509L9 6H12V5C12 4.48716 11.614 4.06449 11.1166 4.00673L11 4ZM12 8H9C8.48716 8 8.06449 8.38604 8.00673 8.88338L8 9V12H11C11.5128 12 11.9355 11.614 11.9933 11.1166L12 11V8Z" />
    </svg>
  );
}
