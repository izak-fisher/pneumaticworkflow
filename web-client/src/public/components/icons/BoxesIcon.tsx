/* eslint-disable */
/* prettier-ignore */
import * as React from 'react';

export type TBoxesIconProps = React.SVGAttributes<SVGElement>;

export function BoxesIcon({ fill = 'currentColor', ...rest }: TBoxesIconProps) {
  return (
    <svg width="20" height="20" viewBox="0 0 20 20" fill={fill} xmlns="http://www.w3.org/2000/svg" {...rest} >
      <path fillRule="evenodd" clipRule="evenodd" d="M15 11C16.6569 11 18 12.3431 18 14V15C18 16.6569 16.6569 18 15 18H14C12.3431 18 11 16.6569 11 15V14C11 12.3431 12.3431 11 14 11H15ZM6 11C7.65685 11 9 12.3431 9 14V15C9 16.6569 7.65685 18 6 18H5C3.34315 18 2 16.6569 2 15V14C2 12.3431 3.34315 11 5 11H6ZM15 13H14C13.4477 13 13 13.4477 13 14V15C13 15.5523 13.4477 16 14 16H15C15.5523 16 16 15.5523 16 15V14C16 13.4477 15.5523 13 15 13ZM6 13H5C4.44772 13 4 13.4477 4 14V15C4 15.5523 4.44772 16 5 16H6C6.55228 16 7 15.5523 7 15V14C7 13.4477 6.55228 13 6 13ZM6 2C7.65685 2 9 3.34315 9 5V6C9 7.65685 7.65685 9 6 9H5C3.34315 9 2 7.65685 2 6V5C2 3.34315 3.34315 2 5 2H6ZM15 2C16.6569 2 18 3.34315 18 5V6C18 7.65685 16.6569 9 15 9H14C12.3431 9 11 7.65685 11 6V5C11 3.34315 12.3431 2 14 2H15ZM6 4H5C4.44772 4 4 4.44772 4 5V6C4 6.55228 4.44772 7 5 7H6C6.55228 7 7 6.55228 7 6V5C7 4.44772 6.55228 4 6 4ZM15 4H14C13.4477 4 13 4.44772 13 5V6C13 6.55228 13.4477 7 14 7H15C15.5523 7 16 6.55228 16 6V5C16 4.44772 15.5523 4 15 4Z" />
    </svg>
  );
}
